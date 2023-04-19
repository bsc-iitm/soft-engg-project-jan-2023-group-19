<template>
  <div class="container">
    <StudentNavBar></StudentNavBar>
    <section class="text-gray-600 body-font relative">
      <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-col text-center w-full mb-12">
          <h1
            class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900"
          >
            Create Ticket
          </h1>
        </div>
        <div class="lg:w-1/2 md:w-2/3 mx-auto">
          <div class="flex flex-wrap -m-2">
            <div class="p-2 w-full">
              <div class="relative">
                <label for="email" class="leading-7 text-sm text-gray-600"
                  >Subject</label
                >
                <input
                  type="text"
                  id="subject"
                  name="subject"
                  v-model="subject"
                  class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                />
              </div>
            </div>
            <div class="p-2 w-full">
              <div class="relative">
                <label for="message" class="leading-7 text-sm text-gray-600"
                  >Message</label
                >
                <textarea
                  id="message"
                  name="message"
                  v-model="message"
                  class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
                ></textarea>
              </div>
            </div>
            <div class="p-2 w-full">
              <button
                @click="createTicket"
                class="flex mx-auto text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg"
              >
                Button
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
      subject: "",
      message: "",
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
    createTicket() {
      axios
        .post(
          "http://localhost:8000/api/tickets/create",
          {
            subject: this.subject,
            message: this.message,
          },
          {
            headers: {
              "Content-Type": "application/json",
              "Authentication-token": localStorage.getItem("token"),
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          this.$router.push("/student/dashboard");
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
  },
};
</script>
