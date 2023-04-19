<template>
  <div>
    <MainNavBar></MainNavBar>
    <section class="text-gray-600 body-font relative">
      <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-col text-center w-full mb-12">
          <h1
            class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900"
          >
            Register
          </h1>
        </div>
        <div class="lg:w-1/2 md:w-2/3 mx-auto">
          <div class="flex flex-wrap -m-2">
            <div class="p-2 w-1/2">
              <div class="relative">
                <label for="name" class="leading-7 text-sm text-gray-600"
                  >Name</label
                >
                <input
                  type="text"
                  id="first_name"
                  name="first_name"
                  v-model="firstName"
                  placeholder="First Name"
                  class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
            </div>
            <div class="p-2 w-1/2">
              <div class="relative">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Surname</label
                >
                <input
                  type="text"
                  id="last_name"
                  name="last_name"
                  v-model="lastName"
                  placeholder="Last Name"
                  class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
            </div>
            <div class="p-2 w-full">
              <div class="relative">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Email</label
                >
                <input
                  type="email"
                  id="email"
                  name="email"
                  v-model="email"
                  placeholder="Email"
                  class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
            </div>
            <div class="p-2 w-full">
              <div class="relative">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Roll no.:</label
                >
                <input
                  type="text"
                  id="text"
                  name="text"
                  v-model="rollNumber"
                  placeholder="Roll Number"
                  class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
            </div>
            <div class="p-2 w-full">
              <div class="relative">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Password</label
                >
                <input
                  type="password"
                  id="password"
                  name="password"
                  v-model="password"
                  placeholder="Password"
                  class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
            </div>
            <div class="p-2 w-full">
              <button
                @click="submitForm"
                class="flex mx-auto text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg"
              >
                Sign Up
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import MainNavBar from "@/components/MainNavbar.vue";
export default {
  components: { MainNavBar },
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      rollNumber: "",
      password: "",
    };
  },
  methods: {
    submitForm() {
      axios
        .post(
          "http://localhost:8000/api/signup",
          {
            first_name: this.firstName,
            last_name: this.lastName,
            email: this.email,
            roll_number: this.rollNumber,
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
          this.$router.push("/login");
        })
        .catch((error) => {
          alert(error.response.data.message);
        });
    },
  },
};
</script>

<style>
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.signup-form {
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
