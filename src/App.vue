<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  beforeCreate() {
    document.querySelector('body').setAttribute('style', 'margin:0;')
  },
}
</script>

<style>
:root {
	/* COLORS */
	--white: #e9e9e9;
	--gray: #333;
	--orange: #FF8D1A;
	--lightorange: #FFC300;

	/* RADII */
	--button-radius: 0.7rem;

	/* SIZES */
	--max-width: 758px;
	--max-height: 420px;

	font-size: 16px;
	font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
		Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
}
html {
  height: 100%;
}

body {
  display: flex;
  flex-direction: column;
  min-height: 100%;
}
</style>
