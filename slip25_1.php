<?php
// Create a new DOM document
$doc = new DOMDocument('1.0', 'UTF-8');
$doc->formatOutput = true;

// Create the root element
$cricketTeam = $doc->createElement("CricketTeam");

// Create Australia's team
$teamAustralia = $doc->createElement("Team");
$teamAustralia->setAttribute("country", "Australia");

$player1 = $doc->createElement("player", "Steve Smith");
$runs1 = $doc->createElement("runs", "7090");
$wicket1 = $doc->createElement("wicket", "17");

$teamAustralia->appendChild($player1);
$teamAustralia->appendChild($runs1);
$teamAustralia->appendChild($wicket1);

// Append Australia's team to root
$cricketTeam->appendChild($teamAustralia);

// Create India's team
$teamIndia = $doc->createElement("Team");
$teamIndia->setAttribute("country", "India");

$player2 = $doc->createElement("player", "Virat Kohli");
$runs2 = $doc->createElement("runs", "12169");
$wicket2 = $doc->createElement("wicket", "4");
$category = $doc->createElement("category", "Captain");

$teamIndia->appendChild($player2);
$teamIndia->appendChild($runs2);
$teamIndia->appendChild($wicket2);
$teamIndia->appendChild($category);

// Append India's team to root
$cricketTeam->appendChild($teamIndia);

// Append root element to the document
$doc->appendChild($cricketTeam);

// Save the XML file
$doc->save("cricket.xml");

echo "✅ Elements added successfully!";
?>
