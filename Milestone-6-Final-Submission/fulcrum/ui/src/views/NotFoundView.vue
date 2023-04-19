<template>
  <MainNavBar></MainNavBar>
  <div class="page-not-found">
    <h1>Page Not Found</h1>
    <p>We're sorry, but the page you requested could not be found.</p>
  </div>
</template>

<script>
import MainNavBar from "@/components/MainNavbar.vue";
export default {
  components: { MainNavBar },
  name: "FaqView",
};
</script>

<style>
.page-not-found {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  flex-direction: column;
}

h1 {
  font-size: 4rem;
  margin-bottom: 20px;
}

p {
  font-size: 1.5rem;
}
</style>
