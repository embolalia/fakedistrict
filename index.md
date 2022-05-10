## Lorem Ipsum

<form action="" method="get">
    <label for="district">Enter your district:</label>
    <input type="text" id="district" name="district" value="NEW YORK1">
    <input type="submit" value="Check">
</form>
<div id="results" hidden=true>
    In 2020, <div id="district"></div> was won by the <div id="party"></div> with <div id="wonWith"></div> of the vote
    <div id="fake" hidden=true>
        fake
    </div>
    <div id="sketchy" hidden=true>
        sketchy
    </div>
    <div id="real" hidden=true>
        real
    </div>
</div>
Data from <a href="https://electionlab.mit.edu/data">MIT Election Lab</a>
<script src="data.json"></script>
<script src="index.js"></script>