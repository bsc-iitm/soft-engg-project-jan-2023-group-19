<template>
  <StudentNavBar></StudentNavBar>
  <div class="container">
    <div class="flex flex-col text-center w-full mb-12">
      <h1
        class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900"
      >
        Open Tickets
      </h1>
    </div>
    <div
      class="flex flex-col text-center w-full mb-12"
      v-if="open_tickets.length != 0"
    >
      <section class="text-gray-600 body-font overflow-hidden">
        <div class="container px-5 py-24 mx-auto">
          <div
            class="-my-8 divide-y-2 divide-gray-100"
            v-for="ticket in open_tickets"
            :key="ticket.id"
          >
            <div class="py-8 flex flex-wrap md:flex-nowrap">
              <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
                <span class="font-semibold title-font text-gray-700">Date</span>
                <span class="mt-1 text-gray-500 text-sm">{{
                  ticket.created_at
                }}</span>
              </div>
              <div class="md:flex-grow">
                <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                  {{ ticket.subject }}
                </h2>
                <a
                  class="text-indigo-500 inline-flex items-center mt-4"
                  v-bind="{ href: '/student/tickets/' + ticket.id }"
                  >View
                  <svg
                    class="w-4 h-4 ml-2"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path d="M5 12h14"></path>
                    <path d="M12 5l7 7-7 7"></path>
                  </svg>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    <div class="flex flex-col text-center w-full mb-12" v-else>
      <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
          <div
            class="lg:w-2/3 flex flex-col sm:flex-row sm:items-center items-start mx-auto"
          >
            <h1
              class="flex-grow sm:pr-16 text-2xl font-medium title-font text-red-900"
            >
              No open tickets available
            </h1>
          </div>
        </div>
      </section>
    </div>
    <div class="flex flex-col text-center w-full mb-12">
      <h1
        class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900"
      >
        Closed Tickets
      </h1>
    </div>
    <div
      class="flex flex-col text-center w-full mb-12"
      v-if="closed_tickets.length != 0"
    >
      <section class="text-gray-600 body-font overflow-hidden">
        <div class="container px-5 py-24 mx-auto">
          <div
            class="-my-8 divide-y-2 divide-gray-100"
            v-for="ticket in closed_tickets"
            :key="ticket.id"
          >
            <div class="py-8 flex flex-wrap md:flex-nowrap">
              <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
                <span class="font-semibold title-font text-gray-700">Date</span>
                <span class="mt-1 text-gray-500 text-sm">{{
                  ticket.created_at
                }}</span>
              </div>
              <div class="md:flex-grow">
                <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                  {{ ticket.subject }}
                </h2>
                <a
                  class="text-indigo-500 inline-flex items-center mt-4"
                  v-bind="{ href: '/student/tickets/' + ticket.id }"
                  >View
                  <svg
                    class="w-4 h-4 ml-2"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path d="M5 12h14"></path>
                    <path d="M12 5l7 7-7 7"></path>
                  </svg>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    <div class="flex flex-col text-center w-full mb-12" v-else>
      <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
          <div
            class="lg:w-2/3 flex flex-col sm:flex-row sm:items-center items-start mx-auto"
          >
            <h1
              class="flex-grow sm:pr-16 text-2xl font-medium title-font text-red-900"
            >
              No closed tickets available
            </h1>
          </div>
        </div>
      </section>
    </div>
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
      open_tickets: [],
      closed_tickets: [],
    };
  },
  beforeCreate: [
    async function () {
      await axios
        .get("http://localhost:8000/api/tickets/open", {
          headers: {
            "Content-Type": "application/json",
            "Authentication-token": localStorage.getItem("token"),
          },
        })
        .then((response) => {
          this.open_tickets = response.data;
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
    async function () {
      await axios
        .get("http://localhost:8000/api/tickets/closed", {
          headers: {
            "Content-Type": "application/json",
            "Authentication-token": localStorage.getItem("token"),
          },
        })
        .then((response) => {
          this.closed_tickets = response.data;
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
  ],
};
</script>
