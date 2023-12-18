new Vue({
    el: '#questions',
    data: {
        questions: []
    },
    created: function () {
        const vm = this;
        var currentUrl = window.location.pathname;
        const str_test = currentUrl.slice(7, -10);
        const test_id = Number(str_test);
        axios.get(`/api/v1/tests/${test_id}/questions/`)
        .then(function (response){
            vm.questions = response.data
        })
    }
}
)

new Vue({
    el: '#test',
    data: {
        test: {}
    },
    created: function () {
        const vm = this;
        var currentUrl = window.location.pathname;
        const str_test = currentUrl.slice(7, -10);
        const test_id = Number(str_test);
        axios.get(`/api/v1/tests/${test_id}/`)
        .then(function (response){
            vm.test = response.data
        })
        
    }
}
)
