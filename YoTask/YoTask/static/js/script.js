$(document).ready(function () {
    $("input").val("")
    $("textarea").val("")

})

function joinLobby() {
    if($('#joinLobbyInput').val()){
        $.ajax({
            type: 'POST',
            url: '',
            data: { 'pin': $('#joinLobbyInput').val(), },
            success: function (res) {
                console.log(res)
                $('#errorJoinLobbyBlock').html(res)
                $('#errorJoinLobby')[0].classList.remove("d-none")
            }

        });
    }
}

function createLobby() {
    if($('#createLobbyInput').val()){
        $.ajax({
            type: 'POST',
            url: '',
            data: { 'lobby_name': $('#createLobbyInput').val(), },
            success: function (res) {
                $('#createLobbyBlock').html(res)
            }

        });
    }
}

function addRoom() {
    if($('#add_room_name').val() &&
        $('#add_room_description').val()){

        $.ajax({
            type: 'POST',
            url: '',
            data: { 'add_room_name': $('#add_room_name').val() ,
                'add_room_description':$('#add_room_description').val(),
                'add_is_private': $('#add_is_private').is(':checked')},
            success: function (res) {
                console.log(res)
                $('#addRoomModal').modal("hide")
                $('#roomsBlock').html(res)
            }

        });
    }
}

function searchRooms() {
    $.ajax({
        type: 'GET',
        url: '',
        data: {
            'searchRooms': $("#searchRooms").val() == "" ? "all" : $("#searchRooms").val()
        },
        success: function (res) {
            // console.log(res)
            $('#roomsBlock').html(res)
        }
    });
}

function addTask() {
    console.log($("#addTaskAssigne").val())
    if($("#addTaskAssigne").val()!="" && $("#addTaskName").val()!="" && $("#addTaskDescription").val()!=""){

        $.ajax({
            type: 'POST',
            url: '',
            data: {
                'asignee': $("#addTaskAssigne").val(), 'task_title':  $("#addTaskName").val(), 'task_description': $("#addTaskDescription").val()
            },
            success: function (res) {
                // console.log(res)
                $('#tasksBlock').html(res)
            }
        });
    }
}
