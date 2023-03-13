<template>
	<div class="home">
		<div class="column is-12 has-text-centered">
			<h2 class="title is-2">Expense Tracker</h2>
		</div>

		<div class="columns is-multiline">
			<div class="column box is-12">
				<h2 class="title is-4">Input Expenses:</h2>

				<div class="columns">
					<div class="column is-1">
						<p>Name: </p>
					</div>
					<div class="column is-2">
						<input class="input" type="string" placeholder="Name" v-model="name">
					</div>
					<div class="column is-1"></div>
					<div class="column is-1">
						<p>Amount: </p>
					</div>
					<div class="column is-2">
						<input class="input" type="number" placeholder="Amount" v-model="amount">
					</div>
					<div class="column is-1"></div>
					<div class="column is-1">
						<p>Expense Type: </p>
					</div>
					<div class="column is-2">
						<Multiselect v-model="selected_expense_type" track-by="id" label="name" placeholder="Select one"
							:options="expense_types" :close-on-select="true" :searchable="true" :allow-empty="false" />
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Expense from "@/types/Expense";
import ExpenseDataService from "@/services/ExpenseDataService";
import Multiselect from '@suadelabs/vue3-multiselect'
import store from "@/store";

export default defineComponent({
	name: "Home",
	components: {
		Multiselect
	},
	data() {
		return {
			name: '',
			amount: 0,
			expense: store.state.user_expenses,
			selected_expense_type: { "id": 1, "name": "groceries" },
			expense_types: [{ "id": 1, "name": "groceries" }, { "id": 2, "name": "rent" }, { "id": 3, "name": "gas" }, { "id": 4, "name": "drinks" }, { "id": 5, "name": "internet" }, { "id": 6, "name": "electricity" }, { "id": 7, "name": "miscellaneous" }]
		}
	},

});
</script>
