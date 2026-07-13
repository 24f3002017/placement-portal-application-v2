<template>

    <AdminNavbar />
    
    <div class="container mt-5 flex-grow-1">
    
        <h2 class="text-center mb-4">
            Placement Management
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
                    <th>Placement Date</th>
    
                </tr>
    
            </thead>
    
            <tbody>
    
                <tr
                    v-for="(placement,index) in filteredPlacements"
                    :key="placement.id"
                >
    
                    <td>{{ index + 1 }}</td>
                    <td>{{ placement.student }}</td>
                    <td>{{ placement.company }}</td>
                    <td>{{ placement.job }}</td>
                    <td>{{ placement.date }}</td>
    
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

const placements = ref([])
const search = ref("")

function goBack() {
    router.push("/admin-dashboard")
}

async function getPlacements() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            "http://127.0.0.1:5000/api/admin/placements",

            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }

        )

        placements.value = response.data

    }

    catch(error) {

        console.log(error.response)

    }

}

const filteredPlacements = computed(() => {

    return placements.value.filter((placement) => {

        return (

            placement.student.toLowerCase().includes(search.value.toLowerCase()) ||

            placement.company.toLowerCase().includes(search.value.toLowerCase()) ||

            placement.job.toLowerCase().includes(search.value.toLowerCase())

        )

    })

})

onMounted(() => {

    getPlacements()

})

</script>