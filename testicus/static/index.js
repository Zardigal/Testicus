new Vue({
    el: '#index',
    data: {
        tests: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/v1/tests/')
        .then(function (response){
            vm.tests = response.data
        })
    }
}
)