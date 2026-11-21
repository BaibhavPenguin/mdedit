html = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Markdown Elements in HTML 4.01 &amp; CSS 2.1 (Light Mode)</title>
  <style type="text/css">
    /* Base Light Mode Page Styling */
    body {
      background-color: #ffffff;
      color: #24292e;
      font-family: Arial, Helvetica, sans-serif;
      font-size: 16px;
      line-height: 1.6;
      margin: 0 auto;
      padding: 30px 20px;
      max-width: 800px;
    }

    /* Headings (# through ######) */
    h1, h2, h3, h4, h5, h6 {
      color: #111111;
      font-weight: bold;
      line-height: 1.25;
      margin-top: 24px;
      margin-bottom: 16px;
    }

    h1 {
      font-size: 2em;
      border-bottom: 2px solid #eaecef;
      padding-bottom: 8px;
    }

    h2 {
      font-size: 1.5em;
      border-bottom: 1px solid #eaecef;
      padding-bottom: 6px;
    }

    h3 { font-size: 1.25em; }
    h4 { font-size: 1em; }
    h5 { font-size: 0.875em; }
    h6 { font-size: 0.85em; color: #6a737d; }

    /* Paragraphs & Links */
    p {
      margin-top: 0;
      margin-bottom: 16px;
    }

    a {
      color: #0366d6;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    /* Bold, Italic, Strikethrough */
    b, strong { font-weight: bold; }
    i, em { font-style: italic; }
    del, strike { text-decoration: line-through; color: #6a737d; }

    /* Horizontal Rule (---) */
    hr {
      border: 0;
      border-top: 2px solid #e1e4e8;
      height: 0;
      margin: 24px 0;
    }

    /* Blockquotes (>) */
    blockquote {
      margin: 0 0 16px 0;
      padding: 8px 16px;
      color: #586069;
      background-color: #f8f9fa;
      border-left: 4px solid #dfe2e5;
    }

    blockquote p {
      margin-bottom: 0;
    }

    /* Lists (Unordered & Ordered) */
    ul, ol {
      margin-top: 0;
      margin-bottom: 16px;
      padding-left: 32px;
    }

    li {
      margin-bottom: 4px;
    }

    /* Inline Code (`code`) & Code Blocks (```) */
    code {
      font-family: "Courier New", Courier, monospace;
      font-size: 0.9em;
      background-color: #f3f4f6;
      color: #c7254e;
      padding: 2px 5px;
      border: 1px solid #e1e4e8;
    }

    pre {
      font-family: "Courier New", Courier, monospace;
      font-size: 0.9em;
      background-color: #f6f8fa;
      color: #24292e;
      padding: 16px;
      border: 1px solid #e1e4e8;
      overflow: auto;
      line-height: 1.45;
      margin-bottom: 16px;
    }

    pre code {
      background-color: transparent;
      color: inherit;
      padding: 0;
      border: 0;
    }

    /* Tables (| Header | Header |) */
    table {
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 16px;
    }

    th, td {
      border: 1px solid #dfe2e5;
      padding: 8px 13px;
      text-align: left;
    }

    th {
      background-color: #f6f8fa;
      font-weight: bold;
      color: #111111;
    }

    tr.even {
      background-color: #fafbfc;
    }

    /* Images (![alt](url)) */
    img {
      max-width: 100%;
      border: 1px solid #dfe2e5;
      padding: 3px;
      background-color: #ffffff;
    }

    /* Task List Simulation */
    ul.task-list {
      list-style-type: none;
      padding-left: 8px;
    }
  </style>
</head>
<body>

  <h1>MDEdit Test Page(#)</h1>
  <p>Testing the preview of MDEdit Preview</p>

  <h2>Heading Level 2 (##)</h2>
  <h3>Heading Level 3 (###)</h3>
  <h4>Heading Level 4 (####)</h4>
  <h5>Heading Level 5 (#####)</h5>
  <h6>Heading Level 6 (######)</h6>

  <hr>

  <h2>Text Formatting</h2>
  <p>
    You can emphasize text with <b>bold (**text**)</b>, <i>italic (*text*)</i>, or <b><i>bold and italic (***text***)</i></b>. 
    You can also use <del>strikethrough (~~text~~)</del> and inline <code>code (`text`)</code>, or create a <a href="#top">hyperlink ([text](url))</a>.
  </p>

  <h2>Blockquotes</h2>
  <blockquote>
    <p>"This is a blockquote (&gt;). In CSS 2.1, a crisp left border and subtle off-white background distinguish quoted text cleanly in light mode."</p>
  </blockquote>

  <h2>Lists</h2>
  <h3>Unordered List (- or *)</h3>
  <ul>
    <li>First unordered item</li>
    <li>Second unordered item
      <ul>
        <li>Nested list item A</li>
        <li>Nested list item B</li>
      </ul>
    </li>
    <li>Third unordered item</li>
  </ul>

  <h3>Ordered List (1., 2., 3.)</h3>
  <ol>
    <li>First ordered step</li>
    <li>Second ordered step</li>
    <li>Third ordered step</li>
  </ol>

  <h3>Task List (- [ ] / - [x])</h3>
  <ul class="task-list">
    <li><input type="checkbox" checked="checked" disabled="disabled"> Write HTML 4.01 structure</li>
    <li><input type="checkbox" checked="checked" disabled="disabled"> Apply CSS 2.1 light mode styles</li>
    <li><input type="checkbox" disabled="disabled"> Deploy to legacy browser</li>
  </ul>

  <h2>Code Block (```)</h2>
  <pre><code>function greet(name) {
  return "Hello, " + name + "!";
}</code></pre>

  <h2>Tables</h2>
  <table>
    <thead>
      <tr>
        <th>Markdown Syntax</th>
        <th>HTML 4.01 Tag</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code># Heading</code></td>
        <td><code>&lt;h1&gt;</code></td>
        <td>Top-level document heading</td>
      </tr>
      <tr class="even">
        <td><code>**Bold**</code></td>
        <td><code>&lt;b&gt;</code> or <code>&lt;strong&gt;</code></td>
        <td>Strong importance or bold text</td>
      </tr>
      <tr>
        <td><code>*Italic*</code></td>
        <td><code>&lt;i&gt;</code> or <code>&lt;em&gt;</code></td>
        <td>Emphasized or italicized text</td>
      </tr>
      <tr class="even">
        <td><code>&gt; Quote</code></td>
        <td><code>&lt;blockquote&gt;</code></td>
        <td>Indented quotation block</td>
      </tr>
    </tbody>
  </table>

  <h2>Images</h2>
  <p>
    <img src="https://via.placeholder.com/600x120/f6f8fa/24292e?text=Markdown+Image+Placeholder" alt="Sample Placeholder Image">
  </p>

</body>
</html>
"""