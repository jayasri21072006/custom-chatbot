# app/utils.py

import logging, re

def log_error(message):
    """Log an error message."""
    logger = logging.getLogger(__name__)
    logger.error(message)

import re

def format_response(response):

    response = re.sub(r'(?m)^(#+)\s*(.*)', 
                      lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>', 
                      response)

    response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response)
    
    
    response = re.sub(r'\*(.*?)\*', r'<em>\1</em>', response)

    
    response = re.sub(r'(?m)^(?:\d+\.|\-)\s*(.*)', r'<li>\1</li>', response)

   
    response = re.sub(r'(<li>.*?</li>(?:\s*<li>.*?</li>)*)', r'<ul>\1</ul>', response, flags=re.DOTALL)


    response = response.replace('\n', '<br>')

    if "```" in response:
        parts = response.split("```")
        formatted_response = ""
        for i, part in enumerate(parts):
            if i % 2 == 1: 
                formatted_response += f'<pre class="code-block"><code>{part}</code></pre>'
            else:
                formatted_response += part.replace('\n', '<br>')  # Replace newlines with <br>
        return formatted_response

    return response
