% include('header.tpl', title='Prices')
<body>
% for item in inputlist:
    <h3>{{item[0]}}</h3>
    <p>
        RRP:   ${{item[1]}}<br>
        Price: ${{item[2]}} ({{item[3]}})<br>
        Best:  ${{item[4]}} (SAVE {{item[5]}}% = ${{item[6]}})
    </p>
% end
</body>
% include('footer.tpl')