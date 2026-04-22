// Read the code below.
// Write a structured review that:
//     Summarizes the most important concerns and proposed priorities.
//     Calls out concrete issues with clear references to the relevant sections.
//     Explains impact and proposes actionable fixes or alternatives.
//     Optionally group notes under headings like “Major”, “Minor”, and “Nit”.

// Do not rewrite the component; respond with review comments and guidance only.

import { useState, useEffect, useRef } from "react";

interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

interface Post {
  id: number;
  title: string;
  body: string;
  userId: number;
}

export function UserDashboard({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);
  const [posts, setPosts] = useState<Post[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredPosts, setFilteredPosts] = useState<Post[]>([]);
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const fetchCount = useRef(0);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    inputRef.current?.focus();
  });

  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);
  }, []);

  useEffect(() => {
    setLoading(true);
    fetchCount.current++;

    fetch(`https://api.example.com/users/${userId}`)
      .then((res) => res.json())
      .then((data) => {
        setUser(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    if (user) {
      fetch(`https://api.example.com/posts?userId=${user.id}`)
        .then((res) => res.json())
        .then((data) => {
          setPosts(data);
        });
    }
  }, [user]);

  useEffect(() => {
    const filtered = posts.filter(
      (post) =>
        post.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        post.body.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredPosts(filtered);
  }, [searchTerm, posts]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch(`https://api.example.com/users/${userId}`)
        .then((res) => res.json())
        .then((data) => setUser(data));
    }, 30000);

    return () => clearInterval(interval);
  }, []);

  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(e.target.value);
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString();
  };

  const isAdmin = user?.role == "admin";

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div style={{ color: "red" }}>{error}</div>;
  }

  return (
    <div className="dashboard">
      <header>
        <h1>Welcome, {user?.name || "Guest"}</h1>
        <span className={isOnline ? "online" : "offline"}>
          {isOnline ? "🟢 Online" : "🔴 Offline"}
        </span>
        {isAdmin && <span className="admin-badge">Admin</span>}
      </header>

      <div className="search-section">
        <input
          ref={inputRef}
          type="text"
          placeholder="Search posts..."
          value={searchTerm}
          onChange={handleSearch}
        />
        <span>Showing {filteredPosts.length} posts</span>
      </div>

      <div className="posts-list">
        {filteredPosts.map((post) => (
          <article className="post-card">
            <h2>{post.title}</h2>
            <p>{post.body}</p>
            <button onClick={() => alert("Post " + post.id + " clicked")}>
              View Details
            </button>
          </article>
        ))}
      </div>

      {filteredPosts.length === 0 && (
        <p>No posts found matching "{searchTerm}"</p>
      )}

      <footer>
        <p>Debug: Fetched {fetchCount.current} times</p>
      </footer>
    </div>
  );
}