<template>
  <v-app id="inspire">
    <v-container
      class="fill-height"
    >
      <v-row
        justify='center'
      >
        <v-col
          cols=6
        >

          <v-skeleton-loader
            :loading='showTipFormSkeletonLoader'
            transition='scale-transition'
            justify='start'
            type='card-heading'
          >
            <TipFormCard
              v-bind='formCardProps'
              v-show='showTipForm'
            />
          </v-skeleton-loader>
          <v-skeleton-loader
            v-show='showTipFormSkeletonLoader'
            transition='none'
            justify='end'
            type='card'
          />
          <ErrorCard
            v-show='showErrorCard'
            :error_code='error_code'
          />
        </v-col>
      </v-row>
    </v-container>
    <v-footer
      app
    >
      <span>&copy; Amperture 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
import TipFormCard from '@/components/TipFormCard'
import ErrorCard from '@/components/ErrorCard'

  export default {
    props: {
      username: String,
      source: String,
    },

    components: {
      TipFormCard,
      ErrorCard,
    },

    created () {
      this.$store.dispatch('payments/getUserPaymentServer', {
        username: this.$route.params.username
      }).then((response) => {
          this.formCardProps.displayName = response.data.user.display_name
          this.formCardProps.username = response.data.user.username
          this.tipFormState = 'success'
      }).catch((error) => {
          console.log(error.data)
          this.tipFormState = 'error'
          this.error_code = error.response.data.error_display
      })

    },

    methods: {
    },

    computed: {
        showTipFormSkeletonLoader(){
            return this.tipFormState === 'loading'
        },
        showTipForm(){
            return this.tipFormState === 'success'
        },
        showErrorCard(){
            return this.tipFormState === 'error'
        }
    },

    data: () => ({
      drawer: false,

      tipFormState: 'loading',
      error_code: '',
      formCardProps: {
        displayName: "",
        username: "",
        paymentAPIs: ['btcpay']

      },
    }),
  }
</script>

<style>
.tip-username{
  text-shadow: 2px 2px 0 #000,
             -1px -1px 0 #000,
              1px -1px 0 #000,
              -1px 1px 0 #000,
               1px 1px 0 #000;
}

</style>
