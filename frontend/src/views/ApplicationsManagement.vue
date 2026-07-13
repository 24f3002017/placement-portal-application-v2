<template>

    <AdminNavbar />
    
    <div class="container mt-5 flex-grow-1">
    
        <h2 class="text-center mb-4">
            Application Management
        </h2>
    
        <hr>
    
        <div class="row mb-3">
    
            <div class="col-md-6">
    
                <input
                    type="text"
                    class="form-control"
                    placeholder="Search student, company or job"
                    v-model="search"
                >
    
            </div>
    
        </div>
    
        <table class="table table-bordered">
    
            <thead>
    
                <tr>
    
                    <th>SL</th>
                    <th>Student</th>
                    <th>Company</th>
                    <th>Job</th>
                    <th>Applied On</th>
                    <th>Status</th>
    
                </tr>
    
            </thead>
    
            <tbody>
    
                <tr
                    v-for="(application,index) in filteredApplications"
                    :key="application.id"
                >
    
                    <td>{{ index + 1 }}</td>
                    <td>{{ application.student }}</td>
                    <td>{{ application.company }}</td>
                    <td>{{ application.job }}</td>
                    <td>{{ application.date }}</td>
    
                    <td>
    
                        <span
                            class="badge bg-primary"
                        >
                            {{ application.status }}
                        </span>
    
                    </td>
    
                </tr>
    
            </tbody>
    
        </table>
    
        <button
            class="btn btn-secondary"
            @click="goBack"
        >
            ← Back to Dashboard
        </button>
    
    </div>
    
    </template>

<script setup>

import AdminNavbar from "../components/AdminNavbar.vue"
import { ref, computed, onMounted } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const router = useRouter()

const applications = ref([])
const search = ref("")

function goBack() {
    router.push("/admin-dashboard")
}

async function getApplications() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(
            "http://127.0.0.1:5000/api/admin/applications",
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        applications.value = response.data

    }

    catch(error) {

        console.log(error.response)

    }

}

const filteredApplications = computed(() => {

    return applications.value.filter((application) => {

        return (

            application.student.toLowerCase().includes(search.value.toLowerCase()) ||

            application.company.toLowerCase().includes(search.value.toLowerCase()) ||

            application.job.toLowerCase().includes(search.value.toLowerCase())

        )

    })

})

onMounted(() => {

    getApplications()

})

</script>