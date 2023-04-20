<template>
  <StudentNavBar />
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
      <div class="flex flex-col text-center w-full mb-20">
        <h2
          class="text-xs text-indigo-500 tracking-widest font-medium title-font mb-1"
        >
          {{ ticket_data.created_on }}
        </h2>
        <h1
          class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900"
        >
          {{ ticket_data.subject }}
        </h1>
        <section class="text-gray-600 body-font overflow-hidden">
          <div class="container px-5 py-24 mx-auto">
            <div class="-my-8 divide-y-2 divide-gray-100">
              <div
                class="py-8 flex flex-wrap md:flex-nowrap"
                v-for="message in ticket_data.messages"
                :key="message.id"
              >
                <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
                  <span class="font-semibold title-font text-gray-700"
                    >Date</span
                  >
                  <span class="mt-1 text-gray-500 text-sm">{{
                    message[1]
                  }}</span>
                </div>
                <div class="md:flex-grow">
                  <p class="leading-relaxed">
                    {{ message[0] }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </section>
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
    <div class="p-2 w-full">
      <button
        @click="text_back"
        class="flex mx-auto text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg"
      >
        Button
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import StudentNavBar from "@/components/StudentNavBar.vue";
export default {
  name: "DashboardView",
  components: { StudentNavBar },
  data() {
    return {
      ticket_data: null,
      ticket_id: this.$route.params.id,
      message: "",
    };
  },
  beforeMount: [
    async function () {
      await axios
        .get("http://localhost:8000/api/tickets/my/" + this.ticket_id, {
          headers: {
            "Content-Type": "application/json",
            "Authentication-token": localStorage.getItem("token"),
          },
        })
        .then((response) => {
          this.ticket_data = response.data;
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
  ],
  methods: {
    text_back: async function () {
      await axios
        .post(
          "http://localhost:8000/api/tickets/text_back/" + this.ticket_id,
          {
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
          this.ticket_data = response.data;
          this.$router.go();
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
  },
};
</script>
