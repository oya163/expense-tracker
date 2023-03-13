import VueRouter, { Route } from 'vue-router'
import { Store } from 'vuex'

import Expense from "@/types/Expense";
import ExpenseType from "@/types/ExpenseType";

/* eslint-disable */
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare module 'vue/types/vue' {
  interface Vue {
    $router: VueRouter
  }
}
