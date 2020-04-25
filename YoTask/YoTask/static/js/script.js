function joinLobby() {
    if($('#joinLobbyInput').val()){
        $.ajax({
            type: 'POST',
            url: '',
            data: { 'pin': $('#joinLobbyInput').val(), },
            success: function (res) {
                $('#errorJoinLobbyBlock').html(res)
                $('#errorJoinLobby')[0].classList.remove("d-none")
            }

        });
    }
}
