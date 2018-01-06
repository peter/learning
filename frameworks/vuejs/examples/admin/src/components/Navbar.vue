<template lang="html">
  <nav class="navbar navbar-inverse">
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <router-link to="/" class="navbar-brand">
          Vue.js Admin
        </router-link>
      </div>
      <div id="navbar" class="navbar-collapse collapse">
        <ul class="nav navbar-nav">
          <!-- <li>
            <router-link to="/articles">Articles</router-link>
          </li> -->
          <li class="logged-in-user">
            <a href="#" data-toggle="tooltip" title="Logga ut" @click="logout">
              {{userEmail()}}
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import User from '@/services/user'

export default {
  methods: {
    userEmail() {
      const user = User.get()
      return user && user.email
    },
    logout() {
      User.logout()
      setTimeout(() => {
        location.reload(true)
      }, 100)
    }
  }
}
</script>

<style lang="css">
</style>
