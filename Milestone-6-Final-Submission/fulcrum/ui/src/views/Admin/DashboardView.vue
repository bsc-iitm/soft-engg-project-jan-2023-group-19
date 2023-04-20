<template>
  <AdminNavBar />
  <div class="admin_dashboard"></div>
</template>

<script>
import axios from "axios";
import AdminNavBar from "@/components/AdminNavBar.vue";

export default {
  components: { AdminNavBar },
  name: "DashboardView",
  beforeCreate: async function () {
    await axios
      .get("http://localhost:8000/api/profile", {
        headers: {
          "Content-Type": "application/json",
          "Authentication-token": localStorage.getItem("token"),
        },
      })
      .then((response) => {
        if (response.data.role_id != 0) {
          this.$router.push("/dashboard");
        }
      })
      .catch((error) => {
        console.log(error.response.data);
        this.$router.push("/dashboard");
      });
  },
  methods: {
    logout() {
      axios
        .get("http://localhost:8000/api/signout", {
          headers: {
            "Content-Type": "application/json",
            "Authentication-token": localStorage.getItem("token"),
          },
        })
        .then((response) => {
          console.log(response.data);
          localStorage.removeItem("token");
          this.$router.push("/");
        })
        .catch((error) => {
          alert(error.response.data.description);
        });
    },
  },
};
</script>
