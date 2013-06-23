<?php // -*- tab-width:2; indent-tabs-mode:nil -*-


#returns 0 if we've seen a similar tag before in this submission set. 
class StemmingPlugin extends MGWeightingPlugin{
  public $enableOnInstall = true;
	public $hasAdmin = true;


	function score(&$game, &$game_model, &$tags, $score) {
		$python_file = "/Users/etaiklein/Localhost/tiltWorkspace/plugins/metadatagames/www/protected/modules/plugins/modules/weighting/components/DictStem.py";
		$mytag = "";
		$mytags = array();
		$i = 0;

		foreach ($game->request->submissions as $submission) {
			foreach ($tags as $image_id => $image_tags) {
				foreach ($image_tags as $tag => $tag_info) {

					# the path of the python file and the string
					$command = "python $python_file $tag 2>&1";

					#standard fare for popopen
					$pid = popen( $command,"r");

					#we want to add the previous tag
					$mytags[] = $mytag;
					#reads the python output and slices out the appropriate word
					$mytag = substr(fread($pid, 256), 0, -1);
					pclose($pid);
											

					#have we seen this before?
					switch(in_array($mytag, $mytags)){

						#returns 0 if we've seen it before
						case True:
						return 0;
					break;

					#if not, carry on.
						case False:
						#return 10;
					break;
					
					}
						
				}
			}
			break; // we expect only one submission.
		}
		return $score;
	}
}