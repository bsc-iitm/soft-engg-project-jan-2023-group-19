<template>
  <StudentNavBar></StudentNavBar>
  <div class="student_dashboard">
    <section class="text-gray-600 body-font">
      <div class="container px-5 py-24 mx-auto flex flex-col">
        <div class="lg:w-4/6 mx-auto">
          <div class="flex flex-col sm:flex-row mt-10">
            <div class="sm:w-1/3 text-center sm:pr-8 sm:py-8">
              <div
                class="w-20 h-20 rounded-full inline-flex items-center justify-center bg-gray-200 text-gray-400"
              >
                <svg
                  fill="none"
                  stroke="currentColor"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  class="w-10 h-10"
                  viewBox="0 0 24 24"
                >
                  <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <div
                class="flex flex-col items-center text-center justify-center"
              >
                <h2 class="font-medium title-font mt-4 text-gray-900 text-lg">
                  {{ this.user_profile.first_name }}
                  {{ this.user_profile.last_name }}
                </h2>
                <div class="w-12 h-1 bg-indigo-500 rounded mt-2 mb-4"></div>
                <p class="text-base">
                  <strong>Email: </strong>{{ this.user_profile.email }}<br />
                  <strong>Roll no.: </strong>{{ this.user_profile.roll_number
                  }}<br />
                  <strong>Account type.: </strong>Student<br />
                </p>
              </div>
            </div>
            <div
              class="sm:w-2/3 sm:pl-8 sm:py-8 sm:border-l border-gray-200 sm:border-t-0 border-t mt-4 pt-4 sm:mt-0 text-center sm:text-left"
            >
              <h2 class="text-gray-900 text-lg mb-1 font-medium title-font">
                Edit profile
              </h2>
              <div class="relative mb-4">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >First name</label
                >
                <input
                  type="name"
                  id="first_name"
                  name="first_name"
                  v-model.lazy="user_update.first_name"
                  class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
              <div class="relative mb-4">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Last name</label
                >
                <input
                  type="name"
                  id="last_name"
                  name="last_name"
                  v-model.lazy="user_update.last_name"
                  class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
              <div class="relative mb-4">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Email</label
                >
                <input
                  type="email"
                  id="email"
                  name="email"
                  v-model.lazy="user_update.email"
                  class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
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
                  v-model.lazy="user_update.password"
                  class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
              <button
                class="text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg"
                v-on:click="profile_update"
              >
                Update
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
import StudentNavBar from "@/components/StudentNavBar.vue";

export default {
  components: { StudentNavBar },
  name: "DashboardView",
  data() {
    return {
      user_profile: null,
      user_update: {
        first_name: "",
        last_name: "",
        email: "",
        password: "",
      },
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
        if (response.data.role_id != 3) {
          this.$router.push("/dashboard");
        }
        this.user_profile = response.data;
      })
      .catch((error) => {
        console.log(error.response.data);
        this.$router.push("/dashboard");
      });
  },
  methods: {
    profile_update: async function () {
      await axios
        .put("http://localhost:8000/api/profile/update", this.user_update, {
          headers: {
            "Content-Type": "application/json",
            "Authentication-token": localStorage.getItem("token"),
          },
        })
        .then((response) => {
          console.log(response.data.message);
        })
        .catch((error) => {
          console.log(error.message);
          this.$forceUpdate();
        });
    },
  },
};
</script>
