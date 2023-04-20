<template>
  <SupervisorNavBar />
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
        <div class="container mx-auto">
          <div class="flex flex-col text-center w-full mb-12">
            <button
              @click="promote"
              class="flex-shrink-0 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg mt-10 sm:mt-0"
            >
              Promote
            </button>
          </div>
        </div>
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
</template>

<script>
import axios from "axios";
import SupervisorNavBar from "@/components/SupervisorNavBar.vue";
export default {
  name: "DashboardView",
  components: { SupervisorNavBar },
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
        .get("http://localhost:8000/api/tickets/others/" + this.ticket_id, {
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
    promote: async function () {
      await axios
        .put(
          "http://localhost:8000/api/tickets/promote/" + this.ticket_id,
          {},
          {
            headers: {
              "Content-Type": "application/json",
              "Authentication-token": localStorage.getItem("token"),
            },
          }
        )
        .then((response) => {
          console.log(response.data);
          this.$router.push("/supervisor/dashboard");
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
  },
};
</script>
