<template>
  <StudentNavBar></StudentNavBar>
  <div class="container">
    <div class="flex flex-col text-center w-full mb-12">
      <h1
        class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900"
      >
        My Tickets
      </h1>
      <p>Tickets created by you</p>
    </div>
    <div
      class="flex flex-col text-center w-full mb-12"
      v-if="tickets.length != 0"
    >
      <section class="text-gray-600 body-font overflow-hidden">
        <div class="container mx-auto">
          <a
            href="/student/CreateTicket"
            target="_blank"
            class="flex-shrink-0 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg mt-10 sm:mt-0"
          >
            Create new ticket
          </a>
          <div
            class="-my-8 divide-y-2 divide-gray-100 px-20 py-24"
            v-for="ticket in tickets"
            :key="ticket.id"
          >
            <div class="py-8 flex flex-wrap md:flex-nowrap">
              <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
                <span class="font-semibold title-font text-gray-700"
                  >Status</span
                >
                <span class="mt-1 text-gray-500 text-sm">{{
                  ticket.status
                }}</span>
              </div>
              <div class="md:flex-grow">
                <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                  {{ ticket.subject }}
                </h2>
                <p class="leading-relaxed">
                  {{ ticket.created_at }}
                </p>
                <a
                  class="text-indigo-500 inline-flex items-center mt-4"
                  v-bind="{ href: '/student/ViewTicket/' + ticket.id }"
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
              class="flex-grow sm:pr-16 text-2xl font-medium title-font text-gray-900"
            >
              You have not created any ticket until now.
            </h1>
            <a
              href="/student/CreateTicket"
              class="flex-shrink-0 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg mt-10 sm:mt-0"
            >
              Create
            </a>
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
      tickets: [],
    };
  },
  beforeCreate: [
    async function () {
      await axios
        .get("http://localhost:8000/api/tickets/my", {
          headers: {
            "Content-Type": "application/json",
            "Authentication-token": localStorage.getItem("token"),
          },
        })
        .then((response) => {
          this.tickets = response.data;
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
  ],
};
</script>
