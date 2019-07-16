$.setPortCallback("in",onInput);

function onInput(ctx,s) {

    $.out(s.Attributes["polarity"]);
}