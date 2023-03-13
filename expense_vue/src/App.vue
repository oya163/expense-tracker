<template>
	<div id="wrapper">
		<nav class="navbar is-primary is-fixed-top" role="navigation" aria-label="dropdown navigation">
			<div class="navbar-brand has-navbar-fixed-top">
				<router-link to="/" class="navbar-item">
					<strong>Expense Tracker</strong>
				</router-link>
			</div>

			<div class="navbar-menu has-navbar-fixed-top" id="navbar-menu">
				<div class="navbar-start">
					<div class="navbar-item has-dropdown is-hoverable">
						<a class="navbar-item has-text-weight-medium"> Dashboard </a>
					</div>
				</div>

				<div class="navbar-end"></div>
			</div>
		</nav>

		<section class="section mt-5">
			<router-view />
		</section>

		<footer class="footer">
			<p class="has-text-centered">Copyright (c) 2023</p>
		</footer>
	</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
	data() {
		return {
			routeChange: false,
			showDropdown: false,
		};
	},
	mounted() {
		document.title = "Home | ET";

		this.$store.dispatch('getUserExpenses');
		this.$store.dispatch('getExpenseTypes');
	},
});
</script>

<style lang="scss">
@import "../node_modules/bulma";
@import "../node_modules/@suadelabs/vue3-multiselect/dist/vue3-multiselect.css";

.lds-dual-ring {
	display: inline-block;
	width: 80px;
	height: 80px;
}

.lds-dual-ring:after {
	content: " ";
	display: block;
	width: 64px;
	height: 64px;
	margin: 8px;
	border-radius: 50%;
	border: 6px solid #ccc;
	border-color: #ccc transparent #ccc transparent;
	animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
	0% {
		transform: rotate(0deg);
	}

	100% {
		transform: rotate(360deg);
	}
}

.is-loading-bar {
	height: 0;
	overflow: hidden;
	-webkit-transition: all 0.3s;
	transition: all 0.3s;

	&.is-loading {
		height: 80px;
	}
}
</style>
