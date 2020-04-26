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
