async function loadMore(){
    url = '/articles/jsonListView/';
    const response = await fetch(url)
    .then(res => res.json())
    .then(res => {
        return res;
    })

    out = `<div class="col-4">
            <a href="${response.data[0].slug}">
                <div class="card border-dark my-2 text-dark">
                    <img class="card-img-top" 
                    src="/${response.data[0].thumbnail}" 
                    alt="${response.data[0].title} thumbnail">
                    <h4 class="card-title">
                        ${response.data[0].title}
                    </h4>
                    {%if obj.postType != 'media'%}
                        <p class="card-subtitle">
                            ${response.data[0].city},
                        </p>
                        <p class="card-subtitle">
                            ${response.data[0].country}
                        </p>
                    {%endif%}
                    <span>
                        Published on ${response.data[0].publishDate}
                    </span>
                </div>
            </a>
        </div>`

    var div = document.createElement("div");
    div.innerHTML = out
    document.getElementsByClassName('row')[0].appendChild(div);
}







