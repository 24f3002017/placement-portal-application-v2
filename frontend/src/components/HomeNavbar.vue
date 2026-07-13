<template>

    <nav
        class="navbar navbar-expand-lg"
        style="background-color: #7B1113;"
    >

        <div class="container">

            <span class="navbar-brand text-white fw-bold">
                IIT Madras Placement Cell
            </span>

            <div class="ms-auto">

                <router-link
                    to="/login"
                    class="btn btn-light btn-sm me-2"
                >
                    Login
                </router-link>

                <router-link
                    to="/student-register"
                    class="btn btn-outline-light btn-sm me-2"
                >
                    Register
                </router-link>

                <router-link
                    to="/company-register"
                    class="btn btn-outline-light btn-sm"
                >
                    For Employers
                </router-link>

            </div>

        </div>

    </nav>

</template>

<script setup>

</script>