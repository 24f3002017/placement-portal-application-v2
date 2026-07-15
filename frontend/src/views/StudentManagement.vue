<template>

    <AdminNavbar />

    <div class="container mt-5 flex-grow-1">

        <h2 class="text-center mb-4">
            Student Management
        </h2>

        <hr>

        <div class="row mb-3">

            <div class="col-md-6">

                <input
                    type="text"
                    class="form-control"
                    placeholder="Search student, roll no or email"
                    v-model="search"
                >

            </div>

            <div class="col-md-3">

                <select
                    class="form-select"
                    v-model="statusFilter"
                >
                    <option value="all">All</option>
                    <option value="active">Active</option>
                    <option value="inactive">Inactive</option>
                    <option value="blacklisted">Blacklisted</option>
                </select>

            </div>

        </div>

        <div>

        <table class="table table-bordered">

            <thead>

                <tr>

                    <th>SL</th>
                    <th>Name</th>
                    <th>Roll No</th>
                    <th>Email</th>
                    <th>Status</th>
                    <th>Action</th>

                </tr>

            </thead>

            <tbody>

                <tr
                    v-for="(student, index) in filteredStudents"
                    :key="student.id"
                >

                    <td>{{ index + 1 }}</td>
                    <td>{{ student.name }}</td>
                    <td>{{ student.roll_no }}</td>
                    <td>{{ student.email }}</td>

                    <td>

                        <span
                            class="badge"
                            :class="{
                                'bg-success': student.status === 'active',
                                'bg-warning text-dark': student.status === 'inactive',
                                'bg-dark': student.status === 'blacklisted'
                            }"
                        >
                            {{ student.status }}
                        </span>

                    </td>

                    <td>

                        <button
                            class="btn btn-primary btn-sm"
                            @click="viewStudent(student.id)"
                        >
                            View Details
                        </button>

                    </td>

                </tr>

            </tbody>

        </table>

        </div>

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

const students = ref([])

const search = ref("")
const statusFilter = ref("all")

function goBack() {
    router.push("/admin-dashboard")
}

function viewStudent(id) {
    router.push("/admin/student/" + id)
}

async function getStudents() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(
            "http://127.0.0.1:5000/api/admin/students",
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        )

        students.value = response.data

    }

    catch(error){

        console.log(error.response)

    }

}

const filteredStudents = computed(() => {

    return students.value.filter((student) => {

        const matchesSearch =

            student.name.toLowerCase().includes(search.value.toLowerCase()) ||

            student.roll_no.toLowerCase().includes(search.value.toLowerCase()) ||

            student.email.toLowerCase().includes(search.value.toLowerCase())

        const matchesStatus =

            statusFilter.value === "all" ||

            student.status === statusFilter.value

        return matchesSearch && matchesStatus

    })

})

onMounted(() => {
    getStudents()
})

</script>