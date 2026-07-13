<template>

    <AdminNavbar />

    <div class="container mt-5 flex-grow-1">

        <h2 class="text-center mb-4">
            Job Management
        </h2>

        <hr>

        <div class="row mb-3">

            <div class="col-md-6">

                <input
                    type="text"
                    class="form-control"
                    placeholder="Search company or job title"
                    v-model="search"
                >

            </div>

            <div class="col-md-3">

                <select
                    class="form-select"
                    v-model="statusFilter"
                >

                    <option value="all">All</option>
                    <option value="approved">Approved</option>
                    <option value="pending">Pending</option>
                    <option value="rejected">Rejected</option>

                </select>

            </div>

        </div>

        <table class="table table-bordered">

            <thead>

                <tr>

                    <th>SL</th>
                    <th>Company</th>
                    <th>Job Title</th>
                    <th>Salary</th>
                    <th>Deadline</th>
                    <th>Approval</th>
                    <th>Current Status</th>
                    <th>Action</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="(job, index) in filteredJobs"
                    :key="job.id"
                >

                    <td>{{ index + 1 }}</td>

                    <td>{{ job.company }}</td>

                    <td>{{ job.title }}</td>

                    <td>{{ job.salary }}</td>

                    <td>{{ job.deadline }}</td>

                    <td>

                        <span
                            class="badge"
                            :class="{
                                'bg-warning text-dark': job.approval_status==='pending',
                                'bg-success': job.approval_status==='approved',
                                'bg-danger': job.approval_status==='rejected'
                            }"
                        >
                            {{ job.approval_status }}
                        </span>

                    </td>

                    <td>

                        <span
                            class="badge"
                            :class="{
                                'bg-success': job.status==='active',
                                'bg-secondary': job.status==='inactive'
                            }"
                        >
                            {{ job.status }}
                        </span>

                    </td>

                    <td>

                        <button
                            class="btn btn-primary btn-sm"
                            @click="viewJob(job.id)"
                        >
                            View Details
                        </button>

                    </td>

                </tr>

            </tbody>

        </table>

        <div class="mt-3">

            <button
                class="btn btn-secondary"
                @click="goBack"
            >
                ← Back to Dashboard
            </button>

        </div>

    </div>

</template>

<script setup>

import AdminNavbar from "../components/AdminNavbar.vue"
import { ref, computed, onMounted } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const router = useRouter()

const jobs = ref([])

const search = ref("")
const statusFilter = ref("all")

function goBack() {
    router.push("/admin-dashboard")
}

function viewJob(id) {
    router.push("/admin/job/" + id)
}

async function getJobs() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(
            "http://127.0.0.1:5000/api/admin/jobs",
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        jobs.value = response.data

    }

    catch(error) {

        console.log(error.response)

    }

}

const filteredJobs = computed(() => {

    return jobs.value.filter((job) => {

        const matchesSearch =

            job.company.toLowerCase().includes(search.value.toLowerCase()) ||

            job.title.toLowerCase().includes(search.value.toLowerCase())

        const matchesStatus =

            statusFilter.value === "all" ||

            job.approval_status === statusFilter.value

        return matchesSearch && matchesStatus

    })

})

onMounted(() => {

    getJobs()

})

</script>