% include('header.tpl', title='500 Error')
<body>
    <strong>500 Error</strong>
    <p>
        Dang it!  A server error.
    </p>
    <div id="log">
        % for line in output:
            {{line}}
            <br>
        % end
    </div>
</body>
% include('footer.tpl')
