<?php

class WordCheckPlugin extends MGWeightingPlugin{
  public $enableOnInstall = true;
	public $hasAdmin = true;
	
	function score(&$game, &$game_model, &$tags, $score) {
		$TrueWordScore = 2;
		$FalseWordScore = 0;
		$python_file = "/Users/etaiklein/Localhost/tiltWorkspace/plugins/metadatagames/www/protected/modules/plugins/modules/weighting/components/DictCheck.py";
		$is_word = "";
		
		foreach ($game->request->submissions as $submission) {
			foreach ($tags as $image_id => $image_tags) {
				foreach ($image_tags as $tag => $tag_info) {
					
							
					# the path of the python file and the string
					$command = "python $python_file $tag 2>&1";
					#opens the connection between the python and php files
					
					#reads from the buffer
					$pid = popen( $command,"r");
					$is_word = substr(fread($pid, 256), 0, -1);				
					pclose($pid);

						
					#change the scores based on the outcome
					switch($is_word){
						case "True":
							$this->addScore($tags[$image_id][$tag], $TrueWordScore);
							$score = $score + $TrueWordScore;
								
							break;

						case "False":
							$this->addScore($tags[$image_id][$tag], $FalseWordScore);
							$score = $score + $FalseWordScore;
							break;
					}
				}
			}
			break; // we expect only one submission.
		}
		return $score;
	}
}
