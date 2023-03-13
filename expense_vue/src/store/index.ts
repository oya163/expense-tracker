import { createStore } from 'vuex';

import ExpenseDataService from "@/services/ExpenseDataService";
import ExpenseTypeDataService from "@/services/ExpenseTypeDataService";
import Expense from "@/types/Expense";
import ExpenseType from "@/types/ExpenseType";
import ResponseData from "@/types/ResponseData";

import apiClient from "@/http-common";

const store = createStore({
  state: {
    user_expenses: [] as Expense[],
    expense_types: [] as ExpenseType[],
    user_id: 1,
  },
  mutations: {
    setUserExpenses(state, payload) {
      state.user_expenses = payload;
    },
    setExpenseTypes(state, payload) {
      state.expense_types = payload;
    },
  },
  actions: {
    async getUserExpenses({ commit, state }) {
      await ExpenseDataService.get(state.user_id)
        .then((response: ResponseData) => {
          commit("setUserExpenses", response.data);
          console.log(response.data);
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },
    async getExpenseTypes({ commit, state }) {
      await ExpenseTypeDataService.get()
        .then((response: ResponseData) => {
          commit("setExpenseTypes", response.data);
          console.log(response.data);
        })
        .catch((e: Error) => {
          console.log(e);
        });
    },
  },
  modules: {
  }
})

export default store;
