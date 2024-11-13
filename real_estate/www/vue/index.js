
const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            name: "Test",
            property_name: "Ateeq Property",
            property_type: "Banglow",
            status: "sale",
            address: "near Aiwan E shahi",
            grand_total: "2000000000",
            image: "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            city: "Kalaburagi",
            properties: []

        }


    },
    methods: {
        async getproperties() {
            let res = await $.ajax({
                url: 'http://127.0.0.1:8001/api/method/real_estate.www.vue.index.get_properties',
                type: 'GET',

            })
            console.log(res.message),
                this.properties = res.message;
        },
        getRandomProperty() {
            let property = this.properties[Math.floor(Math.random() * this.properties.length)];
            console.log(property);
            this.name = property.name;
            this.property_name = property.property_name;
            this.property_type = property.property_type;
            this.status = property.status;
            this.address = property.address;
            this.grand_total = property.grand_total;
            this.image = property.image;
            this.city = property.city;
        }
    },
    computed: {
        compiledMarkdown() {
            // Any computed properties you may want to add
        }
    },
    mounted() {
        this.getproperties();
    }
});

app.mount('#app');
