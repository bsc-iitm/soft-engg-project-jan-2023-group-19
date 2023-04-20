import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () =>
      import(/* webpackChunkName: "home" */ "../views/HomeView.vue"),
  },
  {
    path: "/faq",
    name: "faq",
    component: () =>
      import(/* webpackChunkName: "faq" */ "../views/FaqView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/LoginView.vue"),
  },
  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/register",
    name: "SignUp",
    component: () =>
      import(/* webpackChunkName: "signup" */ "../views/RegisterView.vue"),
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: () =>
      import(/* webpackChunkName: "dashboard" */ "../views/DashboardView.vue"),
  },
  {
    path: "/student/dashboard",
    name: "student dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Student/DashboardView.vue"
      ),
  },
  {
    path: "/student/tickets",
    name: "TicketView",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Student/TicketsView.vue"
      ),
  },
  {
    path: "/student/CreateTicket",
    name: "student tickets dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Student/CreateTicket.vue"
      ),
  },
  {
    path: "/student/ViewTicket/:id",
    name: "student view ticket",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Student/ViewTicket.vue"
      ),
  },
  {
    path: "/student/tickets/:id",
    name: "student view other's ticket",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Student/ViewOtherTicket.vue"
      ),
  },
  {
    path: "/student/profile",
    name: "student profile",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Student/StudentProfile.vue"
      ),
  },
  {
    path: "/admin/dashboard",
    name: "admin dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Admin/DashboardView.vue"
      ),
  },
  {
    path: "/admin/profile",
    name: "admin profile",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Admin/AdminProfile.vue"
      ),
  },
  {
    path: "/staff/dashboard",
    name: "staff dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Staff/DashboardView.vue"
      ),
  },
  {
    path: "/supervisor/dashboard",
    name: "supervisor dashboard",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Supervisor/DashboardView.vue"
      ),
  },
  {
    path: "/supervisor/profile",
    name: "supervisor profile",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Supervisor/SupervisorProfile.vue"
      ),
  },
  {
    path: "/supervisor/ViewTicket/:id",
    name: "student view ticket",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/Supervisor/ViewOtherTicket.vue"
      ),
  },
  {
    path: "/viewFAQ/:id",
    name: "student view ticket",
    component: () =>
      import(
        /* webpackChunkName: "dashboard" */ "../views/ViewOtherTicket.vue"
      ),
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: () =>
      import(/* webpackChunkName: "not-found" */ "../views/NotFoundView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
