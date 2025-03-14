import { createRouter, createWebHistory } from 'vue-router'; 

import ItemList from '../components/ItemList.vue'; 

 

const routes = [ 

  { path: '/', component: ItemList }, 

]; 

 

const router = createRouter({ 

  history: createWebHistory(), 

  routes, 

}); 

 

export default router; 

 