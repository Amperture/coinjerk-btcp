<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <ProfileSetupCard/>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          sm='12'
          md='6'
        >
          <AlertsSetupCard
          />
        </v-col>
        <v-col
          sm='12'
          md='6'
        >
          <PaymentsSetupCard/>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import ProfileSetupCard from '@/components/ProfileSetupCard'
import AlertsSetupCard from '@/components/AlertsSetupCard'
import PaymentsSetupCard from '@/components/PaymentsSetupCard'

export default {
    name: 'dashboard',

    components: {
      AlertsSetupCard,
      PaymentsSetupCard,
      ProfileSetupCard,
    },

    data: () => ({
    }),
}
</script>

<style>
</style>
