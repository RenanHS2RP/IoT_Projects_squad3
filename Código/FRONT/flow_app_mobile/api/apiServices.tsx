const ApiService = {
    listData: async () => {
      try {
        const response = await fetch(`http://xquad3.pythonanywhere.com/pump/`);
  
        if (!response.ok) {
          throw new Error(`Error fetching user data: ${response.status}`);
        }
  
        const apiData = await response.json();
        return apiData;
      } catch (error) {
        console.error(error);
        return null;
      }
    },
  
    post: async (data: any) => {
      try {
        const response = await fetch(`http://xquad3.pythonanywhere.com/pump/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        });
        console.log('hello');
        
  
        if (!response.ok) {
          throw new Error(`Error updating post: ${response.status}`);
        }
        
  
        const postData = await response.json();
        return postData;
      } catch (error) {
        return error;
      }
    },
  };
  
  export default ApiService;
  