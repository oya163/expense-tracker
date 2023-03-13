import { Store } from 'vuex'


declare module '@vue/runtime-core' {
    // declare your own store states
    interface State {
      user_id: number
    }
  
    // provide typings for `this.$store`
    interface ComponentCustomProperties {
      $store: Store<State>
    }
  }