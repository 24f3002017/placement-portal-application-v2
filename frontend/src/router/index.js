import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import StudentRegister from "../views/StudentRegister.vue";
import CompanyRegister from "../views/CompanyRegister.vue";
import StudentDashboard from "../views/StudentDashboard.vue";
import CompanyDashboard from "../views/CompanyDashboard.vue";
import AdminDashboard from "../views/AdminDashboard.vue";
import CompanyManagement from "../views/CompanyManagement.vue";
import CompanyDetails from "../views/CompanyDetails.vue";
import StudentManagement from "../views/StudentManagement.vue";
import StudentDetails from "../views/StudentDetails.vue";
import JobManagement from "../views/JobManagement.vue";
import JobDetails from "../views/JobDetails.vue";
import ApplicationManagement from "../views/ApplicationsManagement.vue";
import PlacementManagement from "../views/PlacementManagement.vue";
import CreateJob from "../views/CreateJob.vue";
import CompanyJobDetails from "../views/CompanyJobDetails.vue";
import CompanyApplications from "../views/CompanyApplications.vue";
import CompanyApplicationDetails from "../views/CompanyApplicationDetails.vue"

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

  {
    path: "/admin/companies",
    component: CompanyManagement,
  },

  {
    path: "/admin/company/:id",
    component: CompanyDetails,
  },

  {
    path: "/admin/students",
    component: StudentManagement,
  },

  {
    path: "/admin/student/:id",
    component: StudentDetails,
  },

  {
    path: "/admin/jobs",
    component: JobManagement
  },

  {
    path: "/admin/job/:id",
    component: JobDetails
  },

  {
    path: "/admin/applications",
    component: ApplicationManagement,
  },

  {
    path: "/admin/placements",
    component: PlacementManagement,
  },

  {
    path: "/company/create-job",
    component: CreateJob
  },

  {
    path: "/company/job/:id",
    component: CompanyJobDetails
  },

  {
    path: "/company/job/:id/applications",
    component: CompanyApplications
  },

  {
    path: "/company/application/:id",
    component: CompanyApplicationDetails
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});



router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");

  const publicPages = [
    "/",
    "/login",
    "/student-register",
    "/company-register",
  ];

  if (publicPages.includes(to.path)) {
    return next();
  }

  if (!token) {
    return next("/login");
  }

  next();
});

export default router;