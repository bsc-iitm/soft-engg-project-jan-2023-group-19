<template>
  <div class="container">
    <MainNavBar></MainNavBar>
    <div class="login-container">
      <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto flex flex-wrap items-center">
          <div class="lg:w-3/5 md:w-1/2 md:pr-16 lg:pr-0 pr-0">
            <h1 class="title-font font-medium text-3xl text-gray-900">
              Welcome to ticketing system
            </h1>
            <p class="leading-relaxed mt-4">
              Please enter valid credentials to login into your account. If you
              don't have an account you can create new one.
            </p>
          </div>
          <div
            class="lg:w-2/6 md:w-1/2 bg-gray-100 rounded-lg p-8 flex flex-col md:ml-auto w-full mt-10 md:mt-0"
          >
            <h2 class="text-gray-900 text-lg font-medium title-font mb-5">
              Sign In
            </h2>
            <div class="relative mb-4">
              <label for="full-name" class="leading-7 text-sm text-gray-600"
                >Email</label
              >
              <input
                type="email"
                id="email"
                name="email"
                v-model="email"
                class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                required
              />
            </div>
            <div class="relative mb-4">
              <label for="email" class="leading-7 text-sm text-gray-600"
                >Password</label
              >
              <input
                type="password"
                id="password"
                name="password"
                v-model="password"
                class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                required
              />
            </div>
            <button
              class="text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg"
              @click="login"
            >
              Sign in
            </button>
            <p class="text-xs text-gray-500 mt-3">
              Don't have an account?
              <router-link
                to="/register"
                class="text-indigo-500 hover:text-indigo-700"
                >Register</router-link
              >
            </p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MainNavBar from "@/components/MainNavbar.vue";
export default {
  components: { MainNavBar },
  data() {
    return {
      email: "",
      password: "",
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
        console.log(response.data);
        this.$router.push("/dashboard");
      })
      .catch((error) => {
        console.log(error.response.statusText);
      });
  },
  methods: {
    login() {
      axios
        .post(
          "http://localhost:8000/api/signin",
          {
            email: this.email,
            password: this.password,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        )
        .then((response) => {
          alert(response.data.message);
          localStorage.setItem("token", response.data.auth_token);
          this.$router.push("/dashboard");
        })
        .catch((error) => {
          alert(error.response.data.description);
        });
    },
  },
};
</script>
<style>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
}

input {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  font-size: 16px;
  width: 100%;
}

button {
  padding: 10px;
  border-radius: 5px;
  border: none;
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}
</style>
