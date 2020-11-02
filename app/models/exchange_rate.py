from app import db  # noqa: F401
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI


class ExchangeRate(db.Model):
    """ Bitcoin exchange rate

    """

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(3), unique=True, nullable=False)
    name = db.Column(
            db.String(64),
            unique=True,
            nullable=False,
            default='FIAT'
            )

    rate = db.Column(db.Float, nullable=False)
    updated_at = db.Column(
            db.DateTime,
            onupdate=datetime.now,
            default=datetime.now
            )

    def convert_from_bitcoin(self, amount: float, is_sats=False):
        self.check_for_update()
        if is_sats:
            amount = float(amount)/(10**8)
        return amount * self.rate

    def convert_to_bitcoin(self, amount: float, want_sats=False):
        self.check_for_update()
        if want_sats:
            amount = amount*(10**8)
        return amount / self.rate

    def check_for_update(self):
        """
        """
        time_since_update = datetime.now() - self.updated_at
        if time_since_update > timedelta(hours=1):
            rate_dict = CoinGeckoAPI().get_price('bitcoin', self.token)
            self.rate = rate_dict['bitcoin'][self.token]
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_all_exchange_rates(cls):
        if len(cls.query.all()) > 0:
            return
        cg = CoinGeckoAPI()
        fiats = cg.get_supported_vs_currencies()
        price_dict = cg.get_price('bitcoin', fiats)['bitcoin']
        for token, rate in price_dict.items():
            db.session.add(
                    ExchangeRate(
                        token=token,
                        name=token,
                        rate=rate
                        )
                    )
        db.session.commit()
