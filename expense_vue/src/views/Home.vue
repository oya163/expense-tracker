<template>
	<div class="home"></div>
</template>

<script lang="ts">
	import { defineComponent } from "vue";

	export default defineComponent({
		name: "Home",
		components: {
		},
		mounted() {
			document.title = "Home | ET";

			this.$store.dispatch('getUserExpenses');
			this.$store.dispatch('getExpenseTypes');
		},
	});
</script>
