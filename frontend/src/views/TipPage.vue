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
            :loading='loading'
            transition='scale-transition'
            justify='start'
            type='card-heading'
          >
            <TipFormCard
              v-bind='formCardProps'
            />
          </v-skeleton-loader>
          <v-skeleton-loader
            v-show='loading'
            transition='none'
            justify='end'
            type='card'
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

  export default {
    props: {
      username: String,
      source: String,
    },
    
    components: {
      TipFormCard,
    },

    created () {
      this.$store.dispatch('payments/getUserPaymentServer', {
        username: this.$route.params.username
      }).then((response) => {
          console.log(response.data.user.display_name)
          this.formCardProps.displayName = response.data.user.display_name
          this.loading = false
      }).catch((error) => {
          // TODO Do something a little more with the error,
          // maybe redirect to a 404?
          console.log(error)
          this.formCardProps.displayName = "user_not_found"
          this.loading = false
      })

    },

    methods: {
    }, 

    data: () => ({
      drawer: false,

      loading: true,
      formCardProps: {
        displayName: "blahblah",
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
