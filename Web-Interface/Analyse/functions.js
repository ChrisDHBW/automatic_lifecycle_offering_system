document.addEventListener('DOMContentLoaded', function() {
    axios.get('/system/statistics')
        .then(response => {
            const data = response.data;
            document.getElementById('average-response-time').textContent = data.averageResponseTime + ' Minuten';
            document.getElementById('accepted-percentage').textContent = data.acceptedPercentage + '%';
            document.getElementById('open-offers').textContent = data.openOffers;
            document.getElementById('sent-offers').textContent = data.sentOffers;

            const rejectedOffersList = document.getElementById('rejected-offers');
            rejectedOffersList.innerHTML = '';
            data.rejectedOffers.forEach(offer => {
                const li = document.createElement('li');
                li.className = 'list-group-item';
                li.textContent = offer;
                rejectedOffersList.appendChild(li);
            });

            document.getElementById('average-devices').textContent = data.averageDevices;
        })
        .catch(error => {
            console.error('Error fetching statistics:', error);
        });
});