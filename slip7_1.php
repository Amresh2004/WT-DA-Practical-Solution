<?php
$dom=new DOMDocument();
$dom->load("Movie.xml");
echo "<h2>Title Of Movie</h2>";
$movietitle=$dom->getElementsByTagName("MovieTitle");
$actorname=$dom->getElementsByTagName("ActorName");
foreach($movietitle as $mt)
{
    echo "<b>$mt->textContent<b><br><br>";
}
echo "<h2>Movie Actor Name's</h2>";
foreach($actorname as $an)
{
    echo "<b>$an->textContent<b><br><br>";
}
?>

<!-- Movie.xml -->

<?xml version="1.0" encoding="UTF-8"?>
<MovieInfo>
    <Movie>
        <MovieNo>1</MovieNo>
        <MovieTitle>Inception</MovieTitle>
        <ActorName>Leonardo DiCaprio</ActorName>
        <ReleaseYear>2010</ReleaseYear>
    </Movie>
    <Movie>
        <MovieNo>2</MovieNo>
        <MovieTitle>The Dark Knight</MovieTitle>
        <ActorName>Christian Bale</ActorName>
        <ReleaseYear>2008</ReleaseYear>
    </Movie>
    <Movie>
        <MovieNo>3</MovieNo>
        <MovieTitle>Interstellar</MovieTitle>
        <ActorName>Matthew McConaughey</ActorName>
        <ReleaseYear>2014</ReleaseYear>
    </Movie>
    <Movie>
        <MovieNo>4</MovieNo>
        <MovieTitle>Avatar</MovieTitle>
        <ActorName>Sam Worthington</ActorName>
        <ReleaseYear>2009</ReleaseYear>
    </Movie>
    <Movie>
        <MovieNo>5</MovieNo>
        <MovieTitle>Gladiator</MovieTitle>
        <ActorName>Russell Crowe</ActorName>
        <ReleaseYear>2000</ReleaseYear>
    </Movie>
</MovieInfo>