<template>

    <AdminNavbar />

    <div class="container mt-5 flex-grow-1">

        <h2 class="text-center mb-4">
            Company Management
        </h2>

        <hr>

        <div class="row mb-3">

            <div class="col-md-6">

                <input
                    type="text"
                    class="form-control"
                    placeholder="Search company or industry"
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
                    <th>Industry</th>
                    <th>Website</th>
                    <th>Status</th>
                    <th>Action</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="(company, index) in filteredCompanies"
                    :key="company.id"
                >

                    <td>{{ index + 1 }}</td>
                    <td>{{ company.name }}</td>
                    <td>{{ company.industry }}</td>
                    <td>{{ company.website }}</td>

                    <td>

                        <span
                            class="badge"
                            :class="{
                                'bg-warning text-dark': company.status === 'pending',
                                'bg-success': company.status === 'approved',
                                'bg-danger': company.status === 'rejected'
                            }"
                        >
                            {{ company.status }}
                        </span>

                    </td>

                    <td>

                        <button
                            class="btn btn-primary btn-sm"
                            @click="viewCompany(company.id)"
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

const companies = ref([])

const search = ref("")
const statusFilter = ref("all")

function goBack() {
    router.push("/admin-dashboard")
}

function viewCompany(id) {
    router.push("/admin/company/" + id)
}

async function getCompanies() {

try {

    const token = localStorage.getItem("token")

    const response = await axios.get(

        "http://127.0.0.1:5000/api/admin/companies",

        {

            headers: {

                Authorization: `Bearer ${token}`

            }

        }

    )

    companies.value = response.data

}

catch (error) {

    console.log(error.response)

}

}

const filteredCompanies = computed(() => {

    return companies.value.filter((company) => {

        const matchesSearch =

            company.name.toLowerCase().includes(search.value.toLowerCase()) ||

            company.industry.toLowerCase().includes(search.value.toLowerCase())

        const matchesStatus =

            statusFilter.value === "all" ||

            company.status === statusFilter.value

        return matchesSearch && matchesStatus

    })

})

onMounted(() => {
    getCompanies()
})

</script>