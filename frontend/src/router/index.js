import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import StudentRegister from "../views/StudentRegister.vue";
import CompanyRegister from "../views/CompanyRegister.vue";
import StudentDashboard from "../views/StudentDashboard.vue";
import CompanyDashboard from "../views/CompanyDashboard.vue";
import AdminDashboard from "../views/AdminDashboard.vue";

const routes = [
  {
    path: "/",
    component: Home,
  },

  {
    path: "/login",
    component: Login,
  },

  {
    path: "/student-register",
    component: StudentRegister,
  },

  {
    path: "/company-register",
    component: CompanyRegister,
  },

  {
    path: "/student-dashboard",
    component: StudentDashboard,
  },

  {
    path: "/company-dashboard",
    component: CompanyDashboard,
  },

  {
    path: "/admin-dashboard",
    component: AdminDashboard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;