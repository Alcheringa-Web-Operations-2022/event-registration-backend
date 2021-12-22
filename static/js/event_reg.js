
var team = [];
//select
function select(id){
    document.getElementById(id).classList.toggle("invisible");
    document.getElementById("card" + id).classList.toggle("bg-blue-50")
    document.getElementById("card" + id).classList.toggle("border-red-500") 
    document.getElementById("card" + id).classList.toggle("selected") 
}


document.getElementById('confirm-select').addEventListener("click", function confirmselect(){
    team=[]
    var elements = document.getElementsByClassName("selected");
    for (var i = 0, len = elements.length; i < len; i++) {
        team.push({'id':elements[i].id.slice(4),'image':elements[i].getElementsByTagName('img')[0].src,'name':elements[i].getElementsByTagName('div')[1].getElementsByTagName('div')[0].innerHTML,'email':elements[i].getElementsByTagName('div')[1].getElementsByTagName('div')[1].innerHTML})
    }
    // console.log(team)
    designchip()
    addchip(team)
})
//triggered when modal is started
function modalstart(){
    for (var i = 0; i < document.getElementsByClassName("team_members_card").length; i++) {
        document.getElementsByClassName("team_members_card")[i].getElementsByTagName('div')[0].classList.add('invisible')
        document.getElementsByClassName("team_members_card")[i].classList.remove("bg-blue-50")
        document.getElementsByClassName("team_members_card")[i].classList.remove("border-red-500") 
        document.getElementsByClassName("team_members_card")[i].classList.remove("selected")
    }
    for (var i = 0; i < team.length; i++) {
        document.getElementById(team[i].id).classList.add("invisible");
        document.getElementById("card" + team[i].id).classList.add("bg-blue-50")
        document.getElementById("card" + team[i].id).classList.add("border-red-500") 
        document.getElementById("card" + team[i].id).classList.add("selected") 
    }
}

//redesign chip
function designchip(){
    if (team.length!=0){
        document.getElementById('add_members_old').classList.add('invisible')
        document.getElementById('chip-team').classList.add('border-dotted')
        document.getElementById('chip-team').classList.add('border-2')
    }
    else{
        document.getElementById('add_members_old').classList.remove('invisible')
        document.getElementById('chip-team').classList.remove('border-dotted')
        document.getElementById('chip-team').classList.remove('border-2')
    }
}



//add chip
function addchip(team){
    $('#chip-team').empty()
    $.each(team, function (i) {
        var templateString = `<span
            id="chip${team[i].id}" class="mx-4 my-2 rounded-full text-white bg-red-500 font-semibold text-sm flex align-center cursor-pointer active:bg-gray-300 transition duration-300 ease w-max">
            <img class="rounded-full w-14 h-14 max-w-none" alt="A"
            src="${team[i].image}" />
            <span class="flex items-center px-3 py-2">
            ${team[i].name}<br>${team[i].email}
            </span>
            <button type="button" class="bg-transparent hover focus:outline-none" onclick="deletechip('${team[i].id}')">
            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="times"
                class="svg-inline--fa fa-times w-3 mr-4" role="img" xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 352 512">
                <path fill="currentColor"
                d="M242.72 256l100.07-100.07c12.28-12.28 12.28-32.19 0-44.48l-22.24-22.24c-12.28-12.28-32.19-12.28-44.48 0L176 189.28 75.93 89.21c-12.28-12.28-32.19-12.28-44.48 0L9.21 111.45c-12.28 12.28-12.28 32.19 0 44.48L109.28 256 9.21 356.07c-12.28 12.28-12.28 32.19 0 44.48l22.24 22.24c12.28 12.28 32.2 12.28 44.48 0L176 322.72l100.07 100.07c12.28 12.28 32.2 12.28 44.48 0l22.24-22.24c12.28-12.28 12.28-32.19 0-44.48L242.72 256z">
                </path>
            </svg>
            </button>
        </span>`;
        $('#chip-team').append(templateString);
        if(i==team.length-1){
            var templateString2 = `<span 
                id="add_member_new"  @click="showModal = true;modalstart();" class="mx-4 my-2 rounded-full text-white bg-red-500 font-semibold text-sm flex align-center cursor-pointer active:bg-gray-300 transition duration-300 ease w-max">
                <img class="rounded-full w-14 h-14 max-w-none" alt="A" src="${team[i].image}" />
            </span>`;
                $('#chip-team').append(templateString2);
        }
    })
}

//delete chip
function deletechip(id_team){
    for (var i = 0; i < team.length; i++) {
        if (team[i].id === id_team) {
            team.splice(i, 1);
        }
    }
    addchip(team)
    designchip()
}





//Add member form
$("#add-member-form").submit(function (event) {
    event.preventDefault();
    
    if(team.length==0){
        notifyError("ERROR", "Members can't be zero")
        return
    }
    if((team.length+1)<{{comp.min_members}} || (team.length+1)>{{comp.max_members}}){
        notifyError("ERROR", "Members not within valid range")
        return
    }
    //Enable Loading
    document.getElementById("loading-dot").classList.remove("invisible")
    $.ajax({
        type: "POST",
        data: {
            'members':JSON.stringify(team),
            'teamname':$("#teamname").val(),
            'link':$("#link").val(),
            'description':$("#description").val(),
        },

        headers: {
            "X-CSRFTOKEN": "{{ csrf_token }}"
        },
        success:(data)=>{
            window.location.replace("{%url 'showallcompetitions'%}")
            notifySuccess('You have registered your team for this event successfully')
            document.getElementById("loading-dot").classList.add("invisible")
        }
    })
});