<template>
  <div class="dashboard">
    <h1>Please wait while you are being redirected...</h1>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      role: "",
    };
  },
  beforeCreate: async function () {
    await axios
      .get("http://localhost:8000/api/profile", {
        headers: {
          "Content-Type": "application/json",
          "Authentication-token": localStorage.getItem("token"),
        },
      })
      .then((response) => {
        this.role = response.data.role_id;
      })
      .catch((error) => {
        if (error.response.status !== 200) {
          this.$router.push("/");
        }
      });

    // Use Vue.js router to navigate to the corresponding dashboard
    switch (this.role) {
      case 0:
        window.location.href = "http://localhost:8000/admin";
        break;
      case 3:
        this.$router.push("/student/dashboard");
        break;
      case 2:
        this.$router.push("/staff/dashboard");
        break;
      case 1:
        this.$router.push("/supervisor/dashboard");
        break;
      default:
        this.$router.push("/dashboard");
    }
  },
};
</script>
