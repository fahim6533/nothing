const like_Icon = document.getElementById('like_icon');
const like_Count = document.getElementById('like_count');


like_Icon.onclick = () => {
    const blogId = like_Icon.getAttribute('data-blog');
    const url = `/like_blog/${parseInt(blogId)}/`;
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-type': 'applicatin/json'
        }
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        if(data.liked) {
            like_Icon.classList.remove('empty-heart');
        }
        else {
            like_Icon.classList.add('empty-heart');
        }
        like_Count.innerHTML = data.like_count;
    })
    .catch(error => {
        console.log(error);
    })
}